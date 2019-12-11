select count(*) as count, 'with sentiment' as [status] from dbo.reviews
where sentiment_score is not null
union all
select count(*) as count, 'without sentiment' from dbo.reviews
where sentiment_score is null


