select 
    sum(case when sentiment_score is not null then 1 else 0 end) as 'Sentiment Populated', 
    sum(case when sentiment_score is null then 1 else 0 end) as 'Null Sentiment'
from dbo.reviews with (nolock)



