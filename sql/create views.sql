USE MarketingData;
GO

CREATE VIEW v_ChannelPerformance AS
SELECT 
	channel,
	AVG(CTR) AS Avg_CTR,
	AVG(CPC) AS Avg_CPC,
	AVG(CPA) AS Avg_CPA,
	AVG(Conversion_Rate) AS Avg_Conversion_Rate,
	AVG(ROI) AS Avg_ROI
FROM CampaignData
GROUP BY channel;
GO

CREATE VIEW v_TopCampaigns AS
SELECT
	campaign_id,
	channel,
	SUM(revenue) AS Total_Revenue,
	SUM(cost) AS Total_Cost,
	AVG(ROI) AS Avg_ROI
FROM CampaignData
GROUP BY campaign_id, channel;



