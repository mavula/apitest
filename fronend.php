<?php

if ($_GET["request_type"] == "getitems" && $_GET["resturant_id"])
{
	echo shell_exec("/opy/python/bin/ptyhon api.py $_GET[resturant_id]");
}

?>
