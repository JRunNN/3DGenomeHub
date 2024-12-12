 docker run -e ES_JAVA_OPTS="-Xms512m -Xmx512m"  -e "discovery.type=single-node" \
 --name es-node01 --net elastic -p 9200:9200 -p 9300:9300 -t docker.elastic.co/elasticsearch/elasticsearch:8.10.2


  -v /mnt/lycai/Projects/ActiveLoops/ActiveLoops_api/configs/elasticsearch:/usr/share/elasticsearch/config \



docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.10.2