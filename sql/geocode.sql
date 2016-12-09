-- This assumes that there is a table pluto16v2 in the database
-- that has lat and lng columns
BEGIN;

-- index bbl
create index on dobjobs (bbl);

alter table dobjobs add column lat_coord numeric;
alter table dobjobs add column lng_coord numeric;

update dobjobs
       set lat_coord = pluto_16v2.lat,
       lng_coord = pluto_16v2.lng
from
   pluto_16v2
where
   pluto_16v2.bbl = dobjobs.bbl;

COMMIT;

-- multi-column index
create index on dobjobs (lat_coord, lng_coord);
create index on dobjobs (lat_coord);
create index on dobjobs (lng_coord);
