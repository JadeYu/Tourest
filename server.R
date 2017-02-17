setwd("/Users/jadezhang/Documents/2016-2017_data_science/API_project/Tourest")
source("RTourest.R")

shinyServer(function(input, output){
	output$wait <- renderImage({
		filename <- paste("graphs/wait",sample(1:7,1),".jpg",sep = "")
    		list(src = filename, contentType = 'image/png', width = 600, height = 350, alt = "Uh-oh, the picture's gone Xb")
	}, deleteFile = F)
	observeEvent(input$showA,{
    		output$attractions <-renderTable({show_attractions(input$state, input$city, 15)})
	})
	observeEvent(input$showR,{
    	output$restaurants <-renderTable({show_restaurants(input$Aselection, input$dining_pref, input$radius)})
	})
	#output$restaurants <- eventReactive(input$showR, {
		#renderTable({show_restaurants(input$Aselection, input$dining_pref, input$radius)})
	#})
	observeEvent(input$showU,{
		if(input$same){
			output$url <-renderText({show_url(input$Rselection, input$start, input$start)})
		}else{
			output$url <-renderText({show_url(input$Rselection, input$start, input$end)})
		}
	})
})
