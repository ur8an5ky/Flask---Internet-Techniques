"use strict";

function init_css_properties_before()
{
	document.getElementById("#visualizer").style.width = window.innerWidth.toString(10) + "px";
}

function init_css_properties_after()
{
	document.getElementById("#grid").style.width = (cell_size * grid_size_x).toString(10) + "px";
	document.getElementById("#grid").style.height = (cell_size * grid_size_y).toString(10) + "px";
}

window.onload = function()
{
	init_css_properties_before();
	generate_grid();
	init_css_properties_after();

	window.addEventListener('resize', () =>
	{
		clear();
	});

	menu_event_listeners();

	document.getElementById("#hider").style.visibility= "hidden";
}