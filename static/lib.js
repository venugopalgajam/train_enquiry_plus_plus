console.log("Sanshray");
var station_codes=[];
window.onload=function(){
	// for(var i=0;i<station_list.length;i++)
	// 	station_codes[i]=station_list[i].station_code;
	// $('#src').autocomplete({
	// 	source:station_codes.slice(0,10),
	// 	lookupLimit:10
	// });

	// $('#dst').autocomplete({
	// 	source:station_codes,
	// 	lookupLimit:10
	// });
	var countries = [
		{ value: 'Andorra', data: 'AD' },
		// ...
		{ value: 'Zimbabwe', data: 'ZZ' }
	 ];
	 
	 $('#src').autocomplete({
		 lookup: countries,
		 onSelect: function (suggestion) {
			 alert('You selected: ' + suggestion.value + ', ' + suggestion.data);
		 }
	 });
	console.log("stations are loaded:"+station_codes.length);
}

// $(document).ready(function(){
// $("#src").keypress(function(){
// 	var entry = $("#src")[0].value;
// 	if(entry!=null){

//     	console.log(entry);
//     	var src_station_list = [];

//     	if(entry!= null && entry.length>=0) {
//     		for(var i=0;i<station_list.length;i++) {
    			
// 	        	if (station_list[i].station_code.search(entry) >=0) {
// 	        		src_station_list.push(station_list[i].station_code);
// 	        		console.log(station_list[i].station_code);
// 	        	}
// 	        }
//     	}
// 	}
    	
        
//     });
// });