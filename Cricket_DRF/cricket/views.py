from rest_framework.views import APIView
from .serializers import Score_Serializers
from rest_framework.response import Response
from .models import ScoreCard
from rest_framework import status




class ScoreSheet(APIView):

    def get(self, request):
        scores = ScoreCard.objects.all()
        if scores.exists():
            serializer = Score_Serializers(scores, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Match is not started yet'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer= Score_Serializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetail(APIView):

    def get_by_jersey_no(self, jersey_no):
        return ScoreCard.objects.get(jersey_no=jersey_no)

    def get(self, request, jersey_no):
        try:
            player = self.get_by_jersey_no(jersey_no)            
            serializer = Score_Serializers(player)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ScoreCard.DoesNotExist:
            return Response({'message': 'Jersey number invalid'}, status=status.HTTP_404_NOT_FOUND)
    
    
    def put(self, request, jersey_no):
        try:
            player = self.get_by_jersey_no(jersey_no)
            serializer= Score_Serializers(player, data= request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except ScoreCard.DoesNotExist:
            return Response({'message': 'Jersey number invalid'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, jersey_no):
        try:
            player= self.get_by_jersey_no(jersey_no)
            player.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except ScoreCard.DoesNotExist:
            return Response({'message': 'Player not in current squad'}, status=status.HTTP_404_NOT_FOUND)