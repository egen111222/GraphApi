from graphene_django import DjangoObjectType
from master.models import Master
import graphene
import master.schema

class Query(
	master.schema.Query,
	graphene.ObjectType):
	pass
	
schema = graphene.Schema(query=Query)
