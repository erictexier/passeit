/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/12/02 18:52:23 by etexier           #+#    #+#             */
/*   Updated: 2019/12/02 19:32:48 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int ft_printf(const char *fmt, ...)
{
	va_list 	ap;
	int			result;

	va_start(ap,fmt);
	res = ft_parse_format(fmt, ap);
	end_var(ap);
	return (res);
}

int main()
{
	ft_printf("toto %c\n", 'c')
	return (0);
}