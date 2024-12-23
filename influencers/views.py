from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Influencer, SocialMediaAccount, Manager
from .serializers import InfluencerSerializer, SocialMediaAccountSerializer, ManagerSerializer
from django.db.models import Q


@api_view(['GET', 'POST'])
def influencers_list(request):
    # Retrieve all influencers
    if request.method == 'GET':
        influencers = Influencer.objects.all()
        serializer = InfluencerSerializer(influencers, many=True)
        return Response(serializer.data)

    # Create a new influencer
    elif request.method == 'POST':
        serializer = InfluencerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def influencers_list_filtered(request):

    # Extract filter parameters
    first_name = request.data.get("first_name", "").strip()
    last_name = request.data.get("last_name", "").strip()
    manager = request.data.get("manager", None)


    filters = Q()
    if first_name:
        filters &= Q(first_name__icontains=first_name)
    if last_name:
        filters &= Q(last_name__icontains=last_name)
    if manager is not None:
        filters &= Q(manager=manager)

    # Query the database with filters
    influencers = Influencer.objects.filter(filters)
    serializer = InfluencerSerializer(influencers, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def influencer_detail(request, pk):
    try:
        influencer = Influencer.objects.get(pk=pk)
    except Influencer.DoesNotExist:
        return Response({'error': 'Influencer not found'}, status=status.HTTP_404_NOT_FOUND)

    # Retrieve a single influencer
    if request.method == 'GET':
        serializer = InfluencerSerializer(influencer)
        return Response(serializer.data)

    # Update an influencer
    elif request.method == 'PUT':
        serializer = InfluencerSerializer(influencer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete an influencer
    elif request.method == 'DELETE':
        influencer.delete()
        return Response({'message': 'Influencer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def social_media_account_list(request):
    if request.method == 'GET':
        accounts = SocialMediaAccount.objects.all()
        serializer = SocialMediaAccountSerializer(accounts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialMediaAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def social_media_account_detail(request, pk):
    try:
        account = SocialMediaAccount.objects.get(pk=pk)
    except SocialMediaAccount.DoesNotExist:
        return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialMediaAccountSerializer(account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialMediaAccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return Response({'message': 'Account deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def manager_list(request):
    if request.method == 'GET':
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def manager_detail(request, pk):
    try:
        manager = Manager.objects.get(pk=pk)
    except Manager.DoesNotExist:
        return Response({'error': 'Manager not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ManagerSerializer(manager)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ManagerSerializer(manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        manager.delete()
        return Response({'message': 'Manager deleted successfully'}, status=status.HTTP_204_NO_CONTENT)