function flyIn(target) {
    anime({
      targets: target,
      translateY: '-100%',
      easing: 'easeOutCubic',
      duration: 400
    });
  }
  function flyOut(target) {
    anime({
      targets: target,
      translateY: '100%',
      easing: 'easeInOutCirc',
      duration: 350
    });
  }     