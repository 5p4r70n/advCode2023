package main

import (
	"fmt"
	"os"
	"sync"

	// "strings"
	"encoding/json"
)

type JsonFormat struct{
	Seeds []int `json:"seeds"`
	SeedToSoil []map[string]int `json:"seed-to-soil"`
	SoilToFertilizer []map[string]int `json:"soil-to-fertilizer"`

	FertilizerToWater []map[string]int `json:"fertilizer-to-water map"`
	WaterToLight []map[string]int `json:"water-to-light map"`
	LightToTemperature []map[string]int `json:"light-to-temperature map"`
	TemperatureToHumidity []map[string]int `json:"temperature-to-humidity map"`
	HumidityToLocation []map[string]int `json:"humidity-to-location map"`
}


func findDest(source,dest,_range,input int)int{
	diff:=(source+(_range-1))-input
	return dest+(_range-1)-diff

}

func Looper(i int,data[]map[string]int)int{
	for _,j:=range data{
		if i>=j["source"] && i<=(j["source"]+j["range"]-1){
		
			return findDest(j["source"],j["destination"],j["range"],i)
			
		}

		}
	return i
}

func getLocation(seed int,inputData JsonFormat,lowestNo *int,wg *sync.WaitGroup){
	defer wg.Done()
	soilNo:=Looper(seed,inputData.SeedToSoil)
	fertNo:=Looper(soilNo,inputData.SoilToFertilizer)
	watertNo:=Looper(fertNo,inputData.FertilizerToWater)
	lightNo:=Looper(watertNo,inputData.WaterToLight)
	tempNo:=Looper(lightNo,inputData.LightToTemperature)
	humidNo:=Looper(tempNo,inputData.TemperatureToHumidity)
	location:=Looper(humidNo,inputData.HumidityToLocation)

	// fmt.Println(seed,"->",fertNo,"->",watertNo,"->",lightNo,"->",tempNo,"->",humidNo,"->",location)

	if *lowestNo >location{
		*lowestNo = location
	}
}



func main(){
	var lowestNo = 2122609492
	var inputData JsonFormat
	wg :=sync.WaitGroup{}

	data,_:=os.ReadFile("js.json")
	err:=json.Unmarshal(data,&inputData);if err!=nil{fmt.Println(err)}
	for _i:=0;_i<len(inputData.Seeds);_i+=2{
		wg.Add(1)
		go func(i int) { 
			defer wg.Done()
			for seed:=inputData.Seeds[i];seed<inputData.Seeds[i]+inputData.Seeds[i+1];seed++{
				wg.Add(1)
				go getLocation(seed,inputData,&lowestNo,&wg)
				}
			}(_i)
		fmt.Println(inputData.Seeds[_i])
	}
	wg.Wait()
	fmt.Println("answer :",lowestNo)
}

