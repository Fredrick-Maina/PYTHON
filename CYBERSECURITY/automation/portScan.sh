# You need to find open ports in  localhost, tools to use afterwards nc only


for p in $(seq 1 65535); 
do
	 nc -z -w1 127.0.0.1 $p 2>/dev/null && echo "OPEN $p";
done
