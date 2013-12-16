json.array!(@paintings) do |painting|
  json.extract! painting, :gallery_id, :name, :image
  json.url painting_url(painting, format: :json)
end
