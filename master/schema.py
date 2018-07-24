from graphene_django import DjangoObjectType
from master.models import Master
import graphene
from graphene import relay, ObjectType

class MasterType(DjangoObjectType):
    class Meta:
        model = Master      

class Query(graphene.ObjectType):
    masters = graphene.List(MasterType)

    def resolve_masters(self, info):
        return Master.objects.all()
