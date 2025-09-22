FROM ruby:3.1-slim

RUN apt-get update && apt-get install -y \
  build-essential \
  nodejs \
  npm \
  && rm -rf /var/lib/apt/lists/*

RUN gem update --system && gem install bundler -v "~> 2.4"

WORKDIR /usr/src/app
COPY Gemfile Gemfile.lock ./
RUN bundle install
COPY . .

EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
