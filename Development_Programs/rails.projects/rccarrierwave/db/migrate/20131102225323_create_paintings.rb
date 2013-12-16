class CreatePaintings < ActiveRecord::Migration
  def change
    create_table :paintings do |t|
      t.integer :gallery_id
      t.string :name
      t.string :image, array: true, default: []


      t.timestamps
    end
  end
end
