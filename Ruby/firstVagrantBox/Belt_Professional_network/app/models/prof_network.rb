class ProfNetwork < ApplicationRecord
  belongs_to :user
  belongs_to :friend
end