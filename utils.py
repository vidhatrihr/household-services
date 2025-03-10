def get_avg_ratings(professional):
  # loop over all requests, extract ratings of each
  ratings = [request.ratings for request in professional.service_requests]
  avg_ratings = 0.0
  if len(ratings) > 0:  # can possibly have 0 `rated` requests
    avg_ratings = sum(ratings)/len(ratings)  # ⚠️ division by zero
  return round(avg_ratings, 2)
