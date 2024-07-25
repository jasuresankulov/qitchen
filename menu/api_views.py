from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from .serializers import MenuItemSerializer, ReservationSerializer
from .models import MenuItem, Reservation
from rest_framework import status
# For using a decorators
from rest_framework.response import Response
from rest_framework.decorators import api_view
# For using class-based views
from rest_framework.views import APIView
from django.forms.models import model_to_dict


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]


class ReservationView(APIView):
    permission_classes = [permissions.AllowAny]

    
    def get(self, request, pk=None):
        context = {"request": request}
        if pk:
            reservation = Reservation.objects.get(id=pk)
            reservation = ReservationSerializer(reservation, context=context)
            return Response(reservation.data, status=status.HTTP_200_OK)
        else:
            all_reservations = Reservation.objects.all()
            reservations = ReservationSerializer(all_reservations, many=True, context=context)
            return Response(reservations.data, status=status.HTTP_200_OK)    
   

    def post(self, request):
        context = {"request": request}
        data = ReservationSerializer(data=request.data, context=context)
        # book_names = request.data["book_names"]

        # Save author to the post
        if data.is_valid():
            return Response(data.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        context = {"request": request}
        reservation = Reservation.objects.get(id=pk)
        data = ReservationSerializer(instance=reservation, data=request.data, context=context)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        reservation = Reservation.objects.get(id=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'MENUITEM'])
# def menuItem_view(request):
#     pool = {}
#     for obj in MenuItem.objects.all():
#         pool[obj.id] = model_to_dict(obj)

#     return Response({"data": pool, 'message': 'Hello, world!'}, status=status.HTTP_200_OK)


# class MenuItemView(APIView):
#     def get(self, request):
#         context = {"request": request}
#         all_menuitem = MenuItem.objects.all()
#         menuitem = MenuItemSerializer(all_menuitem, many=True, context=context)
#         return Response(menuitem.data, status=status.HTTP_200_OK)

#     def menuitem(self, request):
#         context = {"request": request}
#         data = MenuItemSerializer(data=request.data, context=context)
#         # Save author to the post
#         if data.is_valid():
#             # HERE WE NEED TO MAKE IT DYNAMIC
#             # THIS LINE MUST BE DELETED LATER or changed to request.user
#             data.validated_data['author'] = User.objects.first()
#             data.save()
#             return Response(data.data, status=status.HTTP_201_CREATED)
        
#     def put(self, request, pk):
#         context = {"request": request}
#         menuitem = MenuItem.objects.get(id=pk)
#         data = MenuItemSerializer(instance=menuitem, data=request.data, context=context)
#         if data.is_valid():
#             data.save()
#             return Response(data.data, status=status.HTTP_200_OK)
#         return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

