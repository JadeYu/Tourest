source("RTourest.R")

shinyServer(function(input, output){
	output$wait <- renderImage({
		filename <- paste("graphs/wait",sample(1:7,1),".jpg",sep = "")
    		list(src = filename, contentType = 'image/png', width = 600, height = 350, alt = "Uh-oh, the picture's gone Xb")
	}, deleteFile = F)
	#do not put input$something within render functions! Will cause instant response in output.
	observeEvent(input$showA,{
		state = input$state
		city = input$city
    		output$attractions <-renderTable({show_attractions(state, city, 15)})
	})
	observeEvent(input$showR,{
	Aselection = input$Aselection
	dining_pref = input$dining_pref
	radius = input$radius
    	output$restaurants <-renderTable({show_restaurants(Aselection, dining_pref, radius)})
	})
	observeEvent(input$showU,{
		Rselection = input$Rselection
		start = input$start
		end = input$end
		if(input$same){
			output$url <-renderUI(a(href=show_url(Rselection, start, start),"Show in Google Map",target="_blank"))
		}else{
			output$url <-renderUI(a(href=show_url(Rselection, start, end),"Show in Google Map",target="_blank"))
		}
	})
})
