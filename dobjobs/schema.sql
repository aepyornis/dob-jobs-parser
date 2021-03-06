create table dobjobs (
  Job text,
  Doc text,
  Borough text,
  House text,
  StreetName text,
  Block text,
  Lot text,
  Bin text,
  JobType text, 
  JobStatus text,
  JobStatusDescription text,
  LatestActionDate date,
  BuildingType text,
  CommunityBoard text,
  Cluster boolean,
  Landmarked boolean,
  AdultEstab boolean,
  LoftBoard boolean,
  CityOwned boolean,
  Littlee boolean,
  PCFiled boolean,
  eFilingFiled boolean,
  Plumbing boolean,
  Mechanical boolean,
  Boiler boolean,
  FuelBurning boolean,
  FuelStorage boolean,
  Standpipe boolean,
  Sprinkler boolean,
  FireAlarm boolean,
  Equipment boolean,
  FireSuppression boolean,
  CurbCut boolean,
  Other boolean,
  OtherDescription text,
  ApplicantsFirstName text,
  ApplicantsLastName text,
  ApplicantProfessionalTitle text,
  ApplicantLicense text,
  ProfessionalCert text,
  PreFilingDate date,
  Paid date,
  FullyPaid date,
  Assigned date,
  Approved date,
  FullyPermitted date,
  InitialCost money,
  TotalEstFee money,
  FeeStatus text,
  ExistingZoningSqft integer,
  ProposedZoningSqft integer,
  HorizontalEnlrgmt boolean,
  VerticalEnlrgmt boolean,
  EnlargementSQFootage integer,
  StreetFrontage integer,
  ExistingNoofStories integer,
  ProposedNoofStories integer,
  ExistingHeight integer,
  ProposedHeight integer,
  ExistingDwelling integer,
  ProposedDwellingUnits integer,
  ExistingOccupancy text,
  ProposedOccupancy text,
  SiteFill text,
  ZoningDist1 text,
  ZoningDist2 text,
  ZoningDist3 text,
  SpecialDistrict1 text,
  SpecialDistrict2 text,
  OwnerType text,
  NonProfit boolean,
  OwnersFirstName text,
  OwnersLastName text,
  OwnersBusinessName text,
  OwnersHouseNumber text,
  OwnersHouseStreetName text,
  City text,
  State text,
  Zip text,
  OwnersPhone text,
  JobDescription text,
  DOBRunDate date,
  bbl char(10),
  id SERIAL PRIMARY KEY
)
