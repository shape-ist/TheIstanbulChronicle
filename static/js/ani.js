function flyIn(target) {
    anime({
      targets: target,
      translateY: '-100%',
      easing: 'easeOutQuad',
      duration: 200
    });
  }
  function flyOut(target) {
    anime({
      targets: target,
      translateY: '100%',
      easing: 'easeInOutCirc',
      duration: 300
    });
  }