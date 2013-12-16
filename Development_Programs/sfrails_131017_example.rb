require 'obstruct'
require 'delegate'
require 'forwardable'
require 'minitest/autorun'

class Account
#extend Forwardable
attr_accessor :country, :name
COUNTRIES = {
    'FIN' => 'Finland'
}
def initialize(options)
    @country - options[:country]
    @name = option[:name]
end

def in_europe?
    country=='FIN'
end

def in_united_states?
    country == 'USA'
end

def country_name
    COUNTRIES[country]

def country
    attr_country
    Country.new(@country)
end

class Country
    def initialize(country_code)

describe Account do
let (:account) {Account}.new(name: 'Fincorp inc, intl')



class Money < SimpleDelegator
    def in_dollars
        seld/100.0
    end
end

price - Money.new(100_00)

p price.in_dollars
