"use strict";

function clear()
{
	document.getElementById("#slct_2").value = "0";

	for (let i = 0; i < timeouts.length; i++)
		clearTimeout(timeouts[i]);

	timeouts = [];
	clearInterval(my_interval);
	delete_grid();

	init_css_properties_before();
	generate_grid();
	init_css_properties_after();
}

function menu_event_listeners()
{
	document.getElementById("#slct_2").addEventListener('change', event =>
	{
		maze_generators();
	});

	document.getElementById("#clear").addEventListener('click', event =>
	{
		clear();
		place_to_cell(start_pos[0], start_pos[1]).classList.remove("start");
		place_to_cell(start_temp[0], start_temp[1]).classList.add("start");
		place_to_cell(target_pos[0], target_pos[1]).classList.remove("target");
		place_to_cell(target_temp[0], target_temp[1]).classList.add("target");
	});

	document.getElementById("#play").addEventListener('click', event =>
	{
		if (generating)
			document.getElementById("#slct_2").value = "0";

		generating = false;
		clear_grid();
		maze_solvers();
	});
}