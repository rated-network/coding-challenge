## Monitoring and Observability

The goal of this exercise is to assess your ability to implement monitoring and observability for a FastAPI application. You will add telemetry, logging, and metrics collection to the application and create a dashboard to display these metrics along with the Service Level Agreement (SLA) status.

### Application Details

You are provided with a FastAPI application that simulates fault injection and delays for a percentage of requests, maintains a request count, and dynamically adjusts fault rates. Assume the following SLAs:
- 99% uptime
- 100ms p99 response time
- Measured in non-overlapping windows of 2,000 requests

### Tasks

Integrate Monitoring and Logging:
- Instrument the FastAPI application to collect telemetry data (request counts, response times, fault occurrences). Edit the code as necessary.
- Implement appropriate tools for metrics collection and visualization.
- Visualize key metrics and SLA statuses on a dashboard.
- Package the solution using Docker and Docker Compose.

### Deliverables

The solution should be in a GitHub repository with an appropriate README.