class Painting < ActiveRecord::Base
    belongs_to :gallery
    mount_uploader :image, ImageUploader
end
