test = {
  'name': 'return-and-print',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def welcome():
          ...     print('Go')
          ...     return 'hello'
          >>> def cal():
          ...     print('Bears')
          ...     return 'world'
          >>> welcome()
          a344033e5d41145ddc2ecba020ecca21
          687c415dafe5ef56622994c5d47f0c53
          # locked
          >>> print(welcome(), cal())
          a344033e5d41145ddc2ecba020ecca21
          54e01e60cd0534843d98b905f4c5207e
          45bac2b863288e1ee362e4bcae4c1d17
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
