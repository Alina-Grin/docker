FROM ruby

RUN apt-get update && apt-get upgrade -y && apt-get install -y sqlite3 build-essential nodejs libpq-dev yarn
RUN gem update && gem install rails && gem install bundler

ONBUILD COPY app /opt/app
ONBUILD WORKDIR /opt/app
ONBUILD EXPOSE 3000
ONBUILD RUN bundle install
ONBUILD RUN rake db:migrate
ONBUILD RUN rake db:seed
