$(document).ready(function () {
    $('#nav_home').addClass('active');
    new TWTR.Widget({
      version: 2,
      type: 'profile',
      id: 'twitter_feed',
      rpp: 6,
      interval: 30000,
      width: 'auto',
      height: 300,
      theme: {
        shell: {
          background: '#ffffff',
          color: '#2e2e2e'
        },
        tweets: {
          background: '#ffffff',
          color: '#6b6b6b',
          links: '#9191ff'
        }
      },
      features: {
        scrollbar: false,
        loop: false,
        live: false,
        behavior: 'all'
      }
    }).render().setUser('masenf').start();
});
