#******************************************************************************#
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: etexier <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 11:32:12 by etexier           #+#    #+#              #
#    Updated: 2019/11/18 18:36:14 by etexier          ###   ########.fr        #
#                                                                              #
#******************************************************************************#

SRCS		= 	srcs/ft_printf.c

DEPENDS		:= $(patsubst %.c,%.d,$(SRCS))

OBJS		= ${SRCS:.c=.o}

CC			= gcc

CFLAGS		= -Wall -Wextra -Werror -I./includes

.c.o:		
			${CC} ${CFLAGS} -MMD -MP -c $< -o ${<:.c=.o}

NAME		=  libftprintf.a

AR			= ar rc

RM			= rm -f

${NAME}:	${OBJS}
			${AR} ${NAME} ${OBJS}

all:		parking

parking:	$(OBJS)
			$(CC) $(CFLAGS) ${LDFLAGS} $^ -o $@

-include $(DEPENDS)

clean:
			${RM} ${OBJS} ${DEPENDS} parking

fclean:		clean
			${RM} ${NAME}

re:			fclean all
