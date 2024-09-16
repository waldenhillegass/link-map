# Link Map

This is a side project I made to display a representation of the Link light rail transit system on a neopixel strip controlled by a raspberry pi. It updates every 15 seconds with live train locations as they move through the system.

Stations are red leds and trains are green leds. Trains that are stopped at stations are yellow.

## Usage

`python3 train_lights.py <your one bus away api key>`

Neopixels are plugged into GPIO pin 18 on a raspberrypi 3


## Getting an API key
Here are instructions for how to get an API key to get the live location of vehicles.

https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd

## Neopixels I used:
https://www.amazon.com/WS2812B-Individual-Addressable-3-2FT144LEDs-Waterproof/dp/B09PBHJG6G?pd_rd_w=P1UOb&content-id=amzn1.sym.4ddee78a-da5c-402d-bae9-88288c5c47aa&pf_rd_p=4ddee78a-da5c-402d-bae9-88288c5c47aa&pf_rd_r=HSXNKCMQHK6WKWJKA83C&pd_rd_wg=HQLVQ&pd_rd_r=72593ded-d5b9-42b3-9788-95bbdaf6e91a&pd_rd_i=B09PBHJG6G&ref_=pd_bap_d_grid_rp_0_1_ec_pd_hp_d_atf_rp_1_t&th=1

