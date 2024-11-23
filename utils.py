def get_avg_ratings(professional):
  ratings = [request.ratings for request in professional.service_requests]
  avg_ratings = 0.0
  if len(ratings) > 0:
    avg_ratings = sum(ratings)/len(ratings)
  return round(avg_ratings, 2)
