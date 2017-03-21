sleep 20
hadoop fs -mkdir /export
hadoop fs -put /vitk/vitk/dat /export/dat
echo "Environment is ready"
cd /vitk/service/;  python service.py
