<?php
clearstatcache('/flag');
echo fileatime('/flag');
readfile('/flag');
clearstatcache('/flag');
echo '--';
echo fileatime('/flag');
