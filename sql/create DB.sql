CREATE DATABASE MarketingData;
GO

USE MarketingData;
GO

CREATE TABLE CampaignData(
	campaign_id NVARCHAR(20),
	channel NVARCHAR(20),
	[date] DATE,
	impressions INT,
	clicks INT,
	cost FLOAT,
	conversions INT,
	revenue FLOAT,
	CTR FLOAT,
	CPC FLOAT,
	CPA FLOAT,
	Conversion_Rate FLOAT,
	ROI FLOAT,
	PRIMARY KEY(campaign_id, [Date]),
	CONSTRAINT UQ_Campaign_Date UNIQUE (campaign_id, [date])
	);