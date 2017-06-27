(define (maxtwo a b c)
  (cond ((= (min a b c) a) (+ b c))
	((= (min a b c) b) (+ a c))
	(else (+ a b))))

(maxtwo 1 2 3)
(maxtwo 3 2 1)
(maxtwo 2 3 1)
