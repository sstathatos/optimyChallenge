<?php

require 'vendor/autoload.php';

use Prometheus\CollectorRegistry;
use Prometheus\RenderTextFormat;
use Prometheus\Storage\InMemory;

$registry = new CollectorRegistry(new InMemory());

$counter = $registry->getOrRegisterCounter('myapp', 'requests_total', 'Total number of requests', ['method', 'endpoint']);
$counter->inc(['GET', '/metrics']);

$gauge = $registry->getOrRegisterGauge('myapp', 'memory_usage_bytes', 'Memory usage in bytes');
$gauge->set(memory_get_usage());

$histogram = $registry->getOrRegisterHistogram('myapp', 'request_duration_seconds', 'Request duration in seconds', ['method', 'endpoint']);
$histogram->observe(random_int(1, 1000) / 1000, ['GET', '/metrics']);

$renderer = new RenderTextFormat();
$result = $renderer->render($registry->getMetricFamilySamples());
header('Content-type: ' . RenderTextFormat::MIME_TYPE);
echo $result;
