(define (ascending? s)
  (cond ((null? s) true)  ; 空列表被认为是升序的
        ((null? (cdr s)) true)  ; 只有一个元素的列表也是升序的
        (else (if (> (car s) (car (cdr s)))
                  false  ; 如果当前元素大于下一个元素，则不是升序
                  (ascending? (cdr s)))))  ; 否则递归检查剩余的列表
)


(define (my-filter pred s)
  (cond ((null? s) nil)  ; 当列表为空，返回空列表
        (else (if (pred (car s))  ; 检查头部元素是否满足谓词
                 (cons (car s) (my-filter pred (cdr s)))  ; 如果满足，将其加入到结果列表
                 (my-filter pred (cdr s)))))  ; 如果不满足，继续检查剩余部分
)

(define (interleave lst1 lst2)
  (cond ((null? lst1) lst2)  ; 如果 lst1 为空，返回 lst2，因为没有更多的 lst1 元素可添加
        (else (cons (car lst1)  ; 否则，取 lst1 的第一个元素
                    (interleave lst2 (cdr lst1))))))  ; 交换 lst1 和 lst2 的角色，并对 lst1 的余下部分递归

(define (no-repeats s)
  (if (null? s)
      nil
      (cons (car s) 
            (no-repeats (filter (lambda (x) (not (= x (car s))))
                                (cdr s))))))

