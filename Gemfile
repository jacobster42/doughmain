source "https://rubygems.org"

# GitHub Pages compatible setup
gem "github-pages", group: :jekyll_plugins
gem "webrick"

# Remove any ruby version specification that might conflict
# Don't specify: ruby "3.1.0" or similar

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?