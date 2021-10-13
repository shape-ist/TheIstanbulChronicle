function flyIn(target) {
    anime({
      targets: target,
      translateY: '-100%',
      easing: 'easeOutQuad',
      duration: 250
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