import graphene
from graphene_django import DjangoObjectType

from .models import Rick
from users.schema import UserType
from links.models import Rick, Vote
from graphql import GraphQLError

class LinkType(DjangoObjectType):
    class Meta:
        model = Rick

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)
    votes = graphene.List(VoteType)

    def resolve_links(self, info, **kwargs):
        return Rick.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
    
    # ...code
#1
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    name = graphene.String()
    status = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        name = graphene.String()
        status = graphene.String()
        posted_by = graphene.Field(UserType)

    def mutate(self, info, url, name, status):
        user = info.context.user or None

        link = Rick(
            url=url,
            name=name,
            status=status,
            posted_by=user,

        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            name=link.name,
            status=link.status,
        )

    #2
    class Arguments:
        url = graphene.String()
        name = graphene.String()
        status = graphene.String()

    #3
    def mutate(self, info, url, name, status):
        link = Rick(url=url, name=name, status=status)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            name=link.name,
            status=link.status,
        )
    
class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            #1
            raise GraphQLError('You must be logged to vote!')

        link = Rick.objects.filter(id=link_id).first()
        if not link:
            #2
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)


#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()