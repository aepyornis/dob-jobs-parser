-- bbl
create index on dobjobs (bbl);

-- Latest Action Date 
create index on dobjobs (LatestActionDate DESC NULLS LAST);
create index on dobjobs (LatestActionDate DESC);	
 
-- jobtype
create index on dobjobs (JobType);
-- job status
create index on dobjobs (JobStatus);
-- community board
create index on dobjobs (CommunityBoard);
-- existing/proposed # of stories
create index on dobjobs (ExistingNoofStories);
create index on dobjobs (ProposedNoofStories);

-- FULL TEXT search columns

-- owner businessname
ALTER TABLE dobjobs ADD COLUMN ownersbusinessname_tsvector tsvector;
UPDATE dobjobs SET ownersbusinessname_tsvector = to_tsvector('english', ownersbusinessname);
CREATE INDEX ownersbusinessname_tsvector_idx ON dobjbos USING GIN (ownersbusinessname_tsvector);

-- owner name
ALTER TABLE dobjobs ADD COLUMN ownername_tsvector tsvector;
UPDATE dobjobs SET ownername_tsvector = to_tsvector('english', ownername);
CREATE INDEX ownername_tsvector_idx ON dobjbos USING GIN (ownername_tsvector);

--job description
ALTER TABLE dobjobs ADD COLUMN jobdescription_tsvector tsvector;
UPDATE dobjobs SET jobdescription_tsvector = to_tsvector('english', JobDescription));
CREATE INDEX jobdescription_tsvector_idx ON dobjbos USING GIN (jobdescription_tsvector);

--applicant name
ALTER TABLE dobjobs ADD COLUMN applicantname_tsvector tsvector;
UPDATE dobjobs SET applicantname_tsvector = to_tsvector('english', applicantname);
CREATE INDEX applicantname_tsvector_idx ON dobjbos USING GIN (applicantname_tsvector);
