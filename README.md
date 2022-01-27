# python-stripe-integration

An backend with stripe payment API integration using Python(FastAPI)


## APIs: 

1. Create charge for card payment
    - POST /api/v1/create_charge
2. Capture the created charge
    - POST /api/v1/capture_charge/:chargeId
3. Create a refund for the created charge
    - POST /api/v1/create_refund/:chargeId
4. Get a List of all charges
    - GET /api/v1/get_charges  
  
  
### API Docuemntation(OpenAPI) 

- http://localhost:8000/docs

The above documentation can be used as a reference and also for sending request for testing.

- Postman Collection link - https://www.getpostman.com/collections/9f21b128835a473b3c77


## How to run

- Install make
- Install docker

### Set env variables

```
STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY
```
- Create a `.env` file to set environment variables
### Using Docker
Run - 
```
    make build_image
    make run_docker
```

Application is accessable in localhost:8000