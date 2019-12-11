USE AirBnBSanFrancisco
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF OBJECT_ID('dbo.reviews') IS NULL
	CREATE TABLE [dbo].[reviews](
		[listing_id] [int] NOT NULL,
		[id] [int] NOT NULL,
		[date] [date] NULL,
		[reviewer_id] [nvarchar](50) NULL,
		[reviewer_name] [nvarchar](50) NULL,
		[comments] [nvarchar](4000) NULL,
		[sentiment_score] [decimal](12, 4) NULL
	) ON [PRIMARY]
GO