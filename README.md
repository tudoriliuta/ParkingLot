# ParkingLot
Simplistic parking management implementation.

Functionality - initialising class ParkingLot with a command argument will return the resulting order of the cars in the parking lot. 

Currently uses 3 command cues: 
  'p' - text following this cue relates to the name of the vehicle that should be parked closest to the exit. 
          Each parked car receives a ticket number, which is incremented with each new parked vehicle. 
  'u' - string integer following this cue relates to the ticket number that should be removed from the parking lot. 
  'c' - re-arranges all parked cars closer to the exit. 
  
Example: 'pRPT9100;pRND3029;pQDD3982;u6847;pDHD9920;u6846;c;' where RND3029 receives ticket number 6846.
Output: 'RPT9100, DHD9920'
