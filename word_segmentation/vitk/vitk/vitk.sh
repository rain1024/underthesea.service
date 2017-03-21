hadoop fs -rm -r /user/root/output.txt
hadoop fs -rm -r /user/root/input.txt
rm -rf output
rm -rf output.txt
hadoop fs -put input.txt /user/root/input.txt
spark-submit target/vn.vitk-3.0.jar -i input.txt -o output.txt
hadoop fs -copyToLocal /user/root/output.txt output
cat output/* >> output.txt