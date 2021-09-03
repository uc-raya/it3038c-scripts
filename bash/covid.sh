DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
ICU=$(echo $DATA | jq '.[0].inIcuCurrently')
VENTILATOR=$(echo $DATA | jq '.[0].onVentilatorCurrently')
TODAY=$(date)


echo "On $TODAY, there were $POSITIVE positive cases, $NEGATIVE negative tests, $DEATH deaths, $ICU cases in the ICU currently and $VENTILATOR patients on a ventilator"
